public class NegativeRadiusException extends CircleException {

    private double radius;

    public NegativeRadiusException(double rad) {

        super("negative radius");
        this.radius = rad;

    }

    public double getRadius() {
        return this.radius;
    }
}
