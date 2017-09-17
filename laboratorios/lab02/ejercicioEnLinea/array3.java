
/**
 * Ejercicios en linea: Array 3 de CodingBat.
 * 
 * @Autores: Alejandro Murillo - Juan Pablo Vidal Correa
 * 
 */
public class array3
{
//maxSpan
 public int maxSpan(int[] nums) {
    if (nums.length > 0){
        int maxSpan = 1;
        for (int i = 0; i < nums.length; i++){
            for (int j = nums.length - 1; j > i; j--){
                if (nums[j] == nums[i]) {
                    int total = (j - i) + 1;
                    if (total > maxSpan){ 
                        maxSpan = total;
                    } 
                }
            }
        }
        return maxSpan;
    } 
    else{ 
        return 0;
    }
}
//fix34
public int[] fix34(int[] nums){
    for (int i = 0; i < nums.length - 1 ; i++)
        if (nums[i] == 3 && nums[i+1] != 4){
        int count = nums[i + 1];
        nums[i + 1] = 4;
             for (int j = i + 2; j < nums.length; j++){
                if (nums[j] == 4){
               nums[j] = count;
         }
        }
    }
    return nums;
}
//fix45
public int[] fix45(int[] nums) {
    for (int i = 0; i < nums.length; i++){
        if (nums[i] == 5 && i == 0 || nums[i] == 5 && nums[i - 1] != 4) {
            for (int j = 0; j < nums.length; j++){
                if (nums[j] == 4 && nums[j + 1] != 5) {
                    int count = nums[j + 1];
                    nums[j + 1] = 5;
                    nums[i] = count;
                    break;
                }
            }
        }
    }
    return nums;
}
//canBalance
public boolean canBalance(int[] nums) {
    for (int i = 0; i < nums.length ; i++) { 
        int side = 0;
        for (int j = 0; j < i; j++){ 
        side += nums[j];
        }
        for (int j = i; j < nums.length; j++){ 
        side -= nums[j];
        }
        if (side == 0){ 
        return true;
        }
    }
    return false;
}
//linearIn
public boolean linearIn(int[] outer, int[] inner){
	boolean notFound;
    for(int inI = 0; inI < inner.length; inI++){
        notFound = true;
        for(int  outI = 0 ; outI < outer.length && notFound; outI++){
            if(inner[inI] == outer[outI]){
                notFound = false;
  		    }
        }    
        if(notFound){
            return false;
  	    }
  }
  return true;
}
}