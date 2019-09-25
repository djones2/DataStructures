package equality;

import java.time.LocalTime;

class CourseSection
{
   private final String prefix;
   private final String number;
   private final int enrollment;
   private final LocalTime startTime;
   private final LocalTime endTime;

   public CourseSection(final String prefix, final String number,
                        final int enrollment, final LocalTime startTime, final LocalTime endTime)
   {
      this.prefix = prefix;
      this.number = number;
      this.enrollment = enrollment;
      this.startTime = startTime;
      this.endTime = endTime;
   }

   public boolean equals(Object other) {
      if(this.getClass() == other.getClass()) {
         boolean pref = this.prefix.equals(((CourseSection)other).prefix);
         boolean num = this.number.equals(((CourseSection)other).number);
         boolean enroll = this.enrollment == ((CourseSection)other).enrollment;
         boolean start = this.startTime.equals(((CourseSection)other).startTime);
         boolean end = this.endTime.equals(((CourseSection)other).endTime);

         return pref && num && enroll && start && end;
      }
      return false;
   }

   public int hashCode() {
      int prefixHash = 0;
      int numberHash = 0;
      int enrollHash = 0;
      int startHash = 0;
      int endHash = 0;

      if (prefix != null) {
         prefixHash = (prefix.hashCode() * 1);
      }
      if (number != null) {
         numberHash = (number.hashCode() * 2);
      }
      if ((Integer)enrollment != null) {
         enrollHash = (((Integer)enrollment).hashCode() * 3);
      }
      if (startTime != null) {
         startHash = (startTime.hashCode() * 4);
      }
      if (endTime != null) {
         endHash = (endTime.hashCode() * 5);
      }
      return prefixHash + numberHash + enrollHash + startHash + endHash;
   }

}