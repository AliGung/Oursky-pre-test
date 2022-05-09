function no_recur(n,cur) {
  if (!(n == parseInt(n))) {               // If n does not equal to an integer, it will eventually become smaller than 2 
    throw "Invalid input"; }
  return cur + 1 - 1 / n }
