public class Lab00
{
   public static void main(String[] args)
   {
	// Declaring variables
	int x = 5;
	String y = "hello";
	double z = 9.8;

	// Creating an array
	int[] nums = {3, 4, -1, 2};
	int numfound;
	
	//Printing the list of variables
	System.out.println("x: " + x + " y: " + y + " z: " + z);

	// For loop to print each value in the number list
	for (int val: nums){
		System.out.println(val);
	}
	
	// Creating numfound variable
	numfound = char_count(y, 'l');

	// Print number of L's found 
	System.out.println("Found: " + numfound);

	// For loop to count to 10
	for (int i = 1; i < 11; i++){
		System.out.print(i + " ");
	}

	// Print a line of whitespace
	System.out.println("");		
   
   }

    /*   
     Helper function to count number of found
     desireable characters in a string.
    */
    public static int char_count(String s, char c)
    {
        int count = 0;
	
	for (int k = 0; k < s.length(); k++){
		if (s.charAt(k) == c){
			count++;
		}
	}
    return count;
    }
}
