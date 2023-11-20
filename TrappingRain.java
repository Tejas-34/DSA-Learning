class Solution {
    public int trap(int[] height) {
        //auxilury array for left higest bar
        int left[] = new int[height.length];
        left[0] = height[0];
        for(int i=1; i<height.length; i++){
            left[i] = Math.max(left[i-1], height[i]);
        }

        //for right most height bar
        int right[] = new int[height.length];
        right[height.length - 1] =  height[height.length - 1];
        for(int i=height.length-2; i>=0; i--){
            right[i] = Math.max(right[i+1] , height[i]);
        } 

        int trapped_rainwater = 0;
        for(int i=0; i<height.length; i++){
            trapped_rainwater += Math.max( (Math.min(left[i],right[i]) - height[i] ) , 0 ); 
        }

        return trapped_rainwater;
    }
}
