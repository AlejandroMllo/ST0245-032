
/**
 * Ejercicios en linea: Recursion 1 de CodingBat.
 * 
 * @Autores: Alejandro Murillo - Juan Pablo Vidal Correa
 * 
 */
public class recursion1
{
//bunnyEars2
public int bunnyEars2(int bunnies){
     if (bunnies == 0){
        return 0;
    }
    else {
        return bunnies + bunnies + (bunnies / 2);
    }
}
//sumDigits
public int sumDigits(int n){
    if (n == 0){
        return 0;
    }
    else{
        return n % 10 + sumDigits(n / 10);
    }
}
//powerN 
public int powerN(int base, int n){
    if ( n == 1){
        return base;
    }
    else if ( n == 0){
        return 1;
    }
    else{
        return base * powerN( base, n - 1);
    }
}
//array6
public boolean array6(int[] nums, int index){
     if (index >= nums.length){ 
        return false;
    }
     else if (nums[index] == 6){  
        return true;
    }
     else{
        return array6(nums, index + 1);
    }
}
//countPairs 
public int countPairs(String str) {
    int contador = 0;
    if(str.length() < 3) {
         return 0;
    }
    else if (str.charAt(0) == str.charAt(2)) {
         contador += 1;
    }
    return contador + countPairs(str.substring(1));
}
}
