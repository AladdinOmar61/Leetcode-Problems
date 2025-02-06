/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */


var twoSum = function (nums, target) {
    let solMap = new Map();
    // creates the map
    for (let i = 0; i < nums.length; i++) {
        solMap.set(nums[i], i);
    }
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (solMap.has(complement) && solMap.get(complement) !== i) {
            return [i, solMap.get(complement)];
        }
    }
    return [];
};

// var twoSum = function (nums, target) {
//     for (let i = 0; i < nums.length; i++) {
//         for (let j = i + 1; j < nums.length; j++) {
//             if (nums[j] === target - nums[i]) {
//                 return [i, j];
//             }
//         }
//     }
//     // Return an empty array if no solution is found
//     return [];
// };