package calculator;

public abstract class BinaryExpression implements Expression{

    private final Expression lft;
    private final Expression rht;
    private final String operand;

    public BinaryExpression(final Expression lft, final Expression rht, String op) {
        this.lft = lft;
        this.rht = rht;
        this.operand = op;
    }

    public String toString()
    {
        return "(" + lft + " " + operand + " " + rht + ")";
    }

    public double evaluate(final Bindings bindings)
    {
        return _applyOperator(lft.evaluate(bindings), rht.evaluate(bindings));
    }

    protected abstract double _applyOperator(double a, double b);

}
