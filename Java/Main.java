import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        int[] nums = {0, 1, 12, 24, 56, 78, 33, 26};

        // Split array into smaller arrays of 2 elements
        List<Integer[]> smallArrays = new ArrayList<>();
        for (int i = 0; i < nums.length; i += 2) {
            Integer[] pair = new Integer[2];
            pair[0] = nums[i];
            // Check if there is a second element; if not, use the first element again
            pair[1] = (i + 1 < nums.length) ? nums[i + 1] : nums[i];
            smallArrays.add(pair);
        }

        // Step 2 & 3: Find the largest number in each pair and append to a new array
        List<Integer> largestNumbers = new ArrayList<>();
        for (Integer[] pair : smallArrays) {
            largestNumbers.add(Math.max(pair[0], pair[1]));
        }

        // Step 4: Find the Largest and second largest numbers
        int largest = Integer.MIN_VALUE;
        int secondLargest = Integer.MIN_VALUE;

        for (int num : largestNumbers) {
            if (num > largest) {
                secondLargest = largest;
                largest = num;
            } else if (num > secondLargest && num != largest) {
                secondLargest = num;
            }
        }

        System.out.println("Largest number: " + largest);
        System.out.println("Second Largest number: " + secondLargest);
    }
}
