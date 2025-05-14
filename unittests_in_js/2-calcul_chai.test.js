const { expect } = require("chai");
const calculateNumber = require("./2-calcul_chai");

describe("Addition", function () {
  it("Sum when both are int", () => {
    expect(calculateNumber("SUM", 1, 3)).to.equal(4);
  });

  it("Sum when a: float", () => {
    expect(calculateNumber("SUM", 1.2, 3)).to.equal(4);
  });

  it("Sum when b: float", () => {
    expect(calculateNumber("SUM", 1, 3.7)).to.equal(5);
  });

  it("Sum when a is rounded up & b is rounded down", () => {
    expect(calculateNumber("SUM", 1.7, 3.2)).to.equal(5);
  });

  it("Sum when a is rounded down & b is rounded up", () => {
    expect(calculateNumber("SUM", 1.2, 3.7)).to.equal(5);
  });

  it("Sum when both are rounded down", () => {
    expect(calculateNumber("SUM", 1.3, 3.1)).to.equal(4);
  });

  it("Sum when both are rounded up", () => {
    expect(calculateNumber("SUM", 1.8, 3.7)).to.equal(6);
  });
});

describe("Subtraction", function () {
  it("Subtract when both are int", () => {
    expect(calculateNumber("SUBTRACT", 1, 3)).to.equal(-2);
  });

  it("Subtract when a: float", () => {
    expect(calculateNumber("SUBTRACT", 1.2, 3)).to.equal(-2);
  });

  it("Subtract when b: float", () => {
    expect(calculateNumber("SUBTRACT", 1, 3.7)).to.equal(-3);
  });

  it("Subtract when a is rounded up & b is rounded down", () => {
    expect(calculateNumber("SUBTRACT", 1.7, 3.2)).to.equal(-1);
  });

  it("Subtract when a is rounded down & b is rounded up", () => {
    expect(calculateNumber("SUBTRACT", 1.2, 3.7)).to.equal(-3);
  });

  it("Subtract when both are rounded down", () => {
    expect(calculateNumber("SUBTRACT", 1.2, 3.2)).to.equal(-2);
  });

  it("Subtract when both are rounded up", () => {
    expect(calculateNumber("SUBTRACT", 1.6, 3.8)).to.equal(-2);
  });
});

describe("Division", function () {
  it("Divide when both are int", () => {
    expect(calculateNumber("DIVIDE", 1, 3)).to.equal(1 / 3);
  });

  it("Divide when a: float", () => {
    expect(calculateNumber("DIVIDE", 1.2, 3)).to.equal(1 / 3);
  });

  it("Divide when b: float", () => {
    expect(calculateNumber("DIVIDE", 1, 3.7)).to.equal(1 / 4);
  });

  it("Divide when a is rounded up & b is rounded down", () => {
    expect(calculateNumber("DIVIDE", 1.7, 3.2)).to.equal(2 / 3);
  });

  it("Divide when a is rounded down & b is rounded up", () => {
    expect(calculateNumber("DIVIDE", 1.2, 3.7)).to.equal(1 / 4);
  });

  it("Divide when both are rounded down", () => {
    expect(calculateNumber("DIVIDE", 1.1, 3.2)).to.equal(1 / 3);
  });

  it("Divide when both are rounded up", () => {
    expect(calculateNumber("DIVIDE", 1.9, 3.6)).to.equal(2 / 4);
  });

  it("Divide when a = 0", () => {
    expect(calculateNumber("DIVIDE", 0, 42)).to.equal(0);
  });

  it("Divide when b = 0", () => {
    expect(calculateNumber("DIVIDE", 42, 0)).to.equal("Error");
  });
});

describe("Error", function () {
  it("Type is not a string", () => {
    expect(calculateNumber(2, 1, 3)).to.equal("Error");
  });
});
