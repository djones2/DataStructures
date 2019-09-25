import java.util.LinkedList;
import java.util.List;
import java.util.Map;

class ExampleMap
{
   public static List<String> highEnrollmentStudents(
      Map<String, List<Course>> courseListsByStudentName, int unitThreshold)
   {
      List<String> overEnrolledStudents = new LinkedList<>();

      /*
         Build a list of the names of students currently enrolled
         in a number of units strictly greater than the unitThreshold.
      */
      int totalUnits = 0;
   
         for(Map.Entry<String, List<Course>> i : courseListsByStudentName.entrySet()){
        	
            totalUnits = 0;

            for (Course c : i.getValue()){
               totalUnits += c.getNumUnits();
            }
            
            if(totalUnits > unitThreshold){
            	
                  overEnrolledStudents.add(i.getKey());
            }            
      }
      return overEnrolledStudents;      
   }
}
