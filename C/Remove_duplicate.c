#include <stdio.h>
#include <math.h>


int removeDuplicates(int* nums, int numsSize){
    if (numsSize == 0) return 0;
    int i = 0;
    for (int j = 1; j < numsSize; j++) {
        if (nums[j] != nums[i]) {
            i++;
            nums[i] = nums[j];
        }
    }
    return i + 1;
}
int main()
{
    int nums[] = {1,1,2,2,3,4,3};
    printf("%d ",removeDuplicates(nums,sizeof(nums)/sizeof(nums[0])));
    
    return 0;
}
