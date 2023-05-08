const twoSum = (nums, target) => {
  const frequencyMap = {};
  let match;

  nums.forEach((num, index) => {
    if (Object.keys(frequencyMap).includes(String(target - num))) {
      match = [index, frequencyMap[target - num]];
    } else {
      frequencyMap[num] = index;
    }
  });

  return match;
}

console.log(twoSum([2, 7, 11, 15], 9));
console.log(twoSum([3, 2, 4], 6));
console.log(twoSum([3, 3], 6));
