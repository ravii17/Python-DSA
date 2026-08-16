import java.util.*;

public class main{

    public static boolean isDuplicatePresent(int[] arr){

       Arrays.sort(arr);
        for(int i = 1; i < arr.length; i++){
            if(arr[i] == arr[i-1]){
                return true;
            }

        }
        return false;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int[] brr = new int[5];

        for(int i = 0; i < brr.length; i++){
            brr[i] = sc.nextInt();
        }
        
        System.out.println(isDuplicatePresent(brr));

    }
}