const ListNode = (val, next) => {
  this.val = (val === undefined ? 0 : val);
  this.next = (next === undefined ? null : next);
};

const mergeTwoLists = (list1, list2) => {
  if (!list1 && !list2) {
    // case 1: both lists are empty
    return list1;
  } else if (!list1 && list2 || list1 && !list2) {
    // case 2: only one list is empty
    return list1 ? list1 : list2;
  } else {
    // case 3: both lists are non-empty
    if (list1.val <= list2.val) {
      // if list1 is smaller or the same, use it as the new head and recurse on the rest
      list1.next = mergeTwoLists(list1.next, list2);
      return list1;
    } else {
      // if list2 is smaller, use it as the new head and recurse on the rest
      list2.next = mergeTwoLists(list2.next, list1);
      return list2;
    }
  }
};
