import java.lang.Math;

public class Point
{
   private double x;
   private double y;

   public Point(double x, double y){
      this.x = x;
      this.y = y;
   }
 
   public double getX(){
      return x;
   }

   public double getY(){
      return y;
   }

   public double getRadius(){
      double xDistance = getX();
      double yDistance = getY();
      double hypotenuse = Math.pow(xDistance, 2) + Math.pow(yDistance, 2);
      return Math.sqrt(hypotenuse);
   }

   public double getAngle(){
      double xDistance = getX();
      double yDistance = getY();
      double angle = Math.atan2(yDistance, xDistance);
      return angle;
   }

   public Point rotate90(){
      double invertY = (getY() * -1);
      Point P = new Point(invertY, getX());
      return P;
   }
}
