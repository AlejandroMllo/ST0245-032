
/**
 * Ejercicios en linea: Array 2 de CodingBat.
 * 
 * @Autores: Alejandro Murillo - Juan Pablo Vidal Correa
 * 
 */
public class array2
{
//sum13
    public int sum13(int[] nums){
    int result = 0;
    for (int i = 0; i < nums.length; i++) {
        if (nums[i] != 13) 
            result += nums[i];
        else if (i <= nums.length ) 
        i++;
    }
    return result;
}
//has22
public boolean has22(int[] nums){
    for (int i = 0; i <= nums.length - 2; i++){
        if (nums[i] == 2 && nums[i + 1] == 2){
            return true;
        }
    }
    return false;
}
//sum28
public boolean sum28(int[] nums){
    int result = 0;
    for (int i = 0; i < nums.length; i++){
        if (nums[i] == 2){ 
            result += 2;
        }
    }
    return result == 8;
}
//isEverywhere
public boolean isEverywhere(int[] nums, int val){
	for(int i = 0; i < nums.length-1; i++){
		if(nums[i] != val && nums[i+1] != val){
			return false;
		}
	}  
	return true;
}
//matchUp
public int matchUp(int[] nums1, int[] nums2){
    int total = 0;
    for (int i = 0; i < nums1.length; i++){
        if(nums1[i] - 2 == nums2[i] || nums1[i] - 1 == nums2[i] 
        || nums1[i] + 1 == nums2[i] || nums1[i] + 2 == nums2[i]){
             total++;
        }
    }  
    return total;
}
}