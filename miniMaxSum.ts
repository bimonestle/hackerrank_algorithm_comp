"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString: string = "";
let inputLines: string[] = [];
let currentLine: number = 0;

process.stdin.on("data", function (inputStdin: string): void {
  inputString += inputStdin;
});

process.stdin.on("end", function (): void {
  inputLines = inputString.split("\n");
  inputString = "";

  main();
});

function readLine(): string {
  return inputLines[currentLine++];
}

/*
 * Complete the 'miniMaxSum' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function miniMaxSum(arr: number[]): void {
  // Write your code here
  const sortedArr: number[] = arr.sort();

  const minArr: number[] = sortedArr.slice(0, arr.length - 1);
  const maxArr: number[] = sortedArr.slice(1, arr.length);

  const minSum: number = minArr.reduce((acc, curr) => acc + curr, 0);
  const maxSum: number = maxArr.reduce((acc, curr) => acc + curr, 0);

  console.log(minSum, maxSum);
}

function main() {
  const arr: number[] = readLine()
    .replace(/\s+$/g, "")
    .split(" ")
    .map((arrTemp) => parseInt(arrTemp, 10));

  miniMaxSum(arr);
}
