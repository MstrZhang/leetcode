const OPENING_BRACKETS = '([{';
const BRACKET_MAP = {
  ')': '(',
  '}': '{',
  ']': '[',
};

const isValid = (s) => {
  const stack = [];

  try {
    s.split('').forEach((bracket) => {
      if (OPENING_BRACKETS.includes(bracket)) {
        stack.push(bracket);
      } else {
        try {
          if (stack.pop() !== BRACKET_MAP[bracket]) {
            throw error;
          }
        } catch (error) {
          throw error;
        }
      }
    });
  } catch (error) {
    return false;
  }

  return stack.length === 0;
}

console.log(isValid("()"))
console.log(isValid("()[]{}"))
console.log(isValid("(]"))

// using try catch to short-circuit the foreach is a little dirty
// the "proper" javascript way would probably be to use a for loop instead
