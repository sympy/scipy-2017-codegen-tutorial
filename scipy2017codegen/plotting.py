import sympy as sym
from sympy.printing.jscode import JavascriptCodePrinter


def batman_equations():

    x = sym.symbols('x', real=True)

    shoulder = ((sym.S(6) * sym.Abs(sym.sqrt(10)) / 7 + (sym.S(3) / 2 -
                sym.Abs(x) / 2)) - (sym.S(6) * sym.Abs(sym.sqrt(10)) / 14) *
                sym.Abs(sym.sqrt(4 - (sym.Abs(x) - 1)**2)))
    cheek = 9 - 8 * sym.Abs(x)
    ear = 3 * sym.Abs(x) + sym.S(3) / 4
    head = 2 + sym.S(2) / 4
    top_wing = 3 * sym.sqrt(-x**2 + 49) / 7
    bottom_wing = -top_wing
    tail = ((sym.Abs(x / 2) - ((3 * sym.sqrt(33) - 7) / 112) * x**2 - 3) +
            sym.sqrt(1 - (sym.Abs(sym.Abs(x) - 2) - 1)**2))

    top = sym.Piecewise(
        (top_wing, x >= 3),
        (shoulder, x >= 1),
        (cheek, x >= sym.S(3) / 4),
        (ear, x >= sym.S(7) / 12),
        (head, x >= -sym.S(7) / 12),
        (ear, x >= -sym.S(3) / 4),
        (cheek, x >= -1),
        (shoulder, x >= -3),
        (top_wing, True))

    bottom = sym.Piecewise(
        (bottom_wing, x >= 4),
        (tail, x >= -4),
        (bottom_wing, True))

    return top, bottom


def batman_equations_heaviside():
    # From : http://mathworld.wolfram.com/BatmanCurve.html

    x = sym.symbols('x', real=True)
    h_ = sym.symbols('h_')

    w = 3 * sym.sqrt(1 - (x / 7)**2)
    l = ((x + 3) / 2 - sym.S(3) / 7 * sym.sqrt(10) * sym.sqrt(4 - (x + 1)**2) +
         sym.S(6) / 7 * sym.sqrt(10))
    r = ((3 - x) / 2 - sym.S(3) / 7 * sym.sqrt(10) * sym.sqrt(4 - (x - 1)**2) +
         sym.S(6) / 7 * sym.sqrt(10))
    f = ((h_ - l) * sym.Heaviside(x + 1, 0) +
         (r - h_) * sym.Heaviside(x - 1, 0) +
         (l - w) * sym.Heaviside(x + 3, 0) +
         (w - r) * sym.Heaviside(x - 3, 0) +
         w)
    f_of = f.xreplace({x: sym.Abs(x + sym.S(1) / 2) +
                       sym.Abs(x - sym.S(1) / 2) + 6})
    h = sym.S(1) / 2 * (f_of - 11 * (x + sym.S(3) / 4) + sym.Abs(x - sym.S(3) / 4))
    f = f.xreplace({h_: h})
    g = (sym.S(1) / 2 * (sym.Abs(x / 2) + sym.sqrt(1 - (sym.Abs(sym.Abs(x) - 2) -
         1)**2) - sym.S(1) / 112 * (3 * sym.sqrt(33) - 7) * x**2 + 3 *
         sym.sqrt(1 - (sym.S(1) / 7 * x)**2) - 3) * ((x + 4) / sym.Abs(x + 4) -
         (x - 4) / sym.Abs(x - 4)) - 3 * sym.sqrt(1 - (x / 7)**2))

    return f, g


def batman_equations_implicit():
    # try different form that seems to have numerical accuracy issues
    # From: https://gist.github.com/traeblain/1487795
    x, y = sym.symbols('x, y')
    eq1 = ((x/7)**2*sym.sqrt(sym.Abs(sym.Abs(x)-3)/(sym.Abs(x)-3))+(y/3)**2*
           sym.sqrt(sym.Abs(y+3/7*sym.sqrt(33))/(y+3/7*sym.sqrt(33)))-1)
    eq2 = (sym.Abs(x/2)-((3*sym.sqrt(33)-7)/112)*x**2-3+
           sym.sqrt(1-(sym.Abs(sym.Abs(x)-2)-1)**2)-y)
    eq3 = (9*sym.sqrt(sym.Abs((sym.Abs(x)-1)*(sym.Abs(x)-.75))/((1-sym.Abs(x))*
           (sym.Abs(x)-.75)))-8*sym.Abs(x)-y)
    eq4 = (3*sym.Abs(x)+.75*sym.sqrt(sym.Abs((sym.Abs(x)-.75)*(sym.Abs(x)-.5))/
           ((.75-sym.Abs(x))*(sym.Abs(x)-.5)))-y)
    eq5 = (2.25*sym.sqrt(sym.Abs((x-.5)*(x+.5))/((.5-x)*(.5+x)))-y)
    eq6 = (6*sym.sqrt(10)/7+(1.5-.5*sym.Abs(x))*sym.sqrt(sym.Abs(sym.Abs(x)-1)/
           (sym.Abs(x)-1))-(6*sym.sqrt(10)/14)*sym.sqrt(4-(sym.Abs(x)-1)**2)-y)

    return eq1, eq2, eq3, eq4, eq5, eq6


class JSHeavisidePrinter(JavascriptCodePrinter):
    """Slight mod to have Heavisides print so they can be plotted."""

    def _print_Heaviside(self, expr):
        # NOTE : expr.rewrite(sym.Piecewise) almost does the right thing.
        P = sym.Piecewise((0, expr.args[0] < 0), (1, expr.args[0] >= 0),
                         (sym.S(1) / 2, True))
        return self._print(P)


js_template = """\

require(['chartjs'], function(chartjs){{

function f(x) {{
    return {top_function}
}};

function g(x) {{
    return {bottom_function}
}};

function linspace(a,b,n) {{
    // From: https://gist.github.com/joates/6584908
    if(typeof n === "undefined") n = Math.max(Math.round(b-a)+1,1);
    if(n<2) {{ return n===1?[a]:[]; }}
    var i,ret = Array(n);
    n--;
    for(i=n;i>=0;i--) {{ ret[i] = (i*b+(n-i)*a)/n; }}
    return ret;
}}

var ctx = document.getElementById("{chart_id}");
var data = {{
    labels: linspace(-7.5, 7.5, 500),
    datasets: [{{
        label: "top",
        function: f,
        borderColor: "rgba(75, 192, 192, 1)",
        data: [],
        fill: false,
        lineTension: 0,
    }},
    {{
        label: "bottom",
        function: g,
        borderColor: "rgba(153, 102, 255, 1)",
        data: [],
        fill: false,
        lineTension: 0,
    }}]
}};

chartjs.Chart.pluginService.register({{
    beforeInit: function(chart) {{
        var data = chart.config.data;
        for (var i = 0; i < data.datasets.length; i++) {{
            for (var j = 0; j < data.labels.length; j++) {{
                var fct = data.datasets[i].function,
                    x = data.labels[j],
                    y = fct(x);
                data.datasets[i].data.push(y);
            }}
        }}
    }}
}});

var myBarChart = new chartjs.Chart(ctx, {{
    type: 'line',
    data: data,
    options: {{
        scales: {{
            yAxes: [{{
                ticks: {{
                    beginAtZero:true
                }}
            }}]
        }}
    }}
}});

}});

element.append("<canvas id='{chart_id}' width='400'></canvas>");\
"""
