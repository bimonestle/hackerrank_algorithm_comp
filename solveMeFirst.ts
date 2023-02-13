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

function main() {
  // Enter your code here

  const firstInteger: number = parseInt(readLine());
  const secondInteger: number = parseInt(readLine());
  if (!firstInteger || !secondInteger) return false;
  const inputValidation = validateInput(firstInteger, secondInteger);

  if (!inputValidation) return false;

  return solveMeFirst(firstInteger, secondInteger);
}

const validateInput = async (firstInteger: number, secondInteger: number) => {
  if (firstInteger <= 1 && firstInteger >= 1000) return false;
  if (secondInteger <= 1 && secondInteger >= 1000) return false;
};

const solveMeFirst = async (firstInteger: number, secondInteger: number) => {
  const result: number = firstInteger + secondInteger;
  const resultInString: string = `${result}`;
  return process.stdout.write(resultInString);
};
