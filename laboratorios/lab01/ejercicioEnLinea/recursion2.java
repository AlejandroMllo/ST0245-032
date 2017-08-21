
/**
 * Ejercicios en linea: Recursion 2 de CodingBat.
 * 
 * @Autores: Alejandro Murillo - Juan Pablo Vidal Correa
 * 
 */
public class recursion2
{
//groupSum6
public boolean groupSum6(int start, int[] nums, int target){
    if(start >= nums.length){
        return target == 0;
    }
    else if(nums[start] == 6){
        return groupSum6(start + 1, nums, target - nums[start]);
    }
    else if(groupSum6(start + 1, nums, target - nums[start])){
        return true;
    }
    else{
        return groupSum6(start + 1, nums, target);
    }
}
//groupNoAdj
public boolean groupNoAdj(int start, int[] nums, int target){
    if (start >= nums.length){
        return (target == 0);
    }
    else if (groupNoAdj(start + 2, nums, target - nums[start])){
        return true;
    }
    return(groupNoAdj(start + 1, nums, target));
}
//groupSum5
public boolean groupSum5(int start, int[] nums, int target){
    if (start >= nums.length){
        return (target == 0);
    }
    else if(nums[start] % 5 == 0){
 		if(start < nums.length - 1 && nums[start+1] == 1){
	 		return groupSum5(start + 2, nums, target - nums[start]);
 		}
	 	return groupSum5(start + 1, nums, target - nums[start]);
    }
    else if(groupSum5(start + 1, nums, target - nums[start])){
        return true;
    }
    return groupSum5(start + 1, nums, target);
}
//groupSumClump (se puede usar un ciclo)
public boolean groupSumClump(int start, int[] nums, int target){
    if(start>=nums.length){
        return target==0;
    }
    int i = start;
    for(i = start;  i < nums.length && nums[start] == nums[i]; i++){ 
        if(groupSumClump(i, nums, target - ((i - start) * nums[start]))){
            return true;
        }
    }
 	return groupSumClump(i, nums, target);	
}
//splitArray
public boolean splitArray(int[] nums){	
  return split( nums, 0, 0);	
}
public boolean split( int[] nums, int side1, int side2){
	if(side1 == nums.length){
		return (side2 == 0);
	}
	if(split(nums, side1 + 1, side2 + nums[side1])){
		return true;
	}
	return split(nums, side1 + 1, side2 - nums[side1]);
}
}
