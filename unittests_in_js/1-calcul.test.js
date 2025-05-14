const assert = require("assert");
const calculateNumber = require("./1-calcul");

describe("Addition", function () {
    it("Sum when both are int", () => {
        assert.strictEqual(calculateNumber("SUM", 1, 3), 4);
    });

    it("Sum when a: float", () => {
        assert.strictEqual(calculateNumber("SUM", 1.2, 3), 4);
    });

    it("Sum when b: float", () => {
        assert.strictEqual(calculateNumber("SUM", 1, 3.7), 5);
    });

    it("Sum when a is rounded up & b is rounded down", () => {
        assert.strictEqual(calculateNumber("SUM", 1.7, 3.2), 5);
    });

    it("Sum when a is rounded down & b is rounded up", () => {
        assert.strictEqual(calculateNumber("SUM", 1.2, 3.7), 5);
    });

    it("Sum when both are rounded down", () => {
        assert.strictEqual(calculateNumber("SUM", 1.3, 3.1), 4);
    });

    it("Sum when both are rounded up", () => {
        assert.strictEqual(calculateNumber("SUM", 1.8, 3.7), 6);
    });
});

describe("Subtraction", function () {
    it("Subtract when both are int", () => {
        assert.strictEqual(calculateNumber("SUBTRACT", 1, 3), -2);
    });

    it("Subtract when a: float", () => {
        assert.strictEqual(calculateNumber("SUBTRACT", 1.2, 3), -2);
    });

    it("Subtract when b: float", () => {
        assert.strictEqual(calculateNumber("SUBTRACT", 1, 3.7), -3);
    });

    it("Subtract when a is rounded up & b is rounded down", () => {
        assert.strictEqual(calculateNumber("SUBTRACT", 1.7, 3.2), -1);
    });

    it("Subtract when a is rounded down & b is rounded up", () => {
        assert.strictEqual(calculateNumber("SUBTRACT", 1.2, 3.7), -3);
    });

    it("Subtract when both are rounded down", () => {
        assert.strictEqual(calculateNumber("SUBTRACT", 1.2, 3.2), -2);
    });

    it("Subtract when both are rounded up", () => {
        assert.strictEqual(calculateNumber("SUBTRACT", 1.6, 3.8), -2);
    });
});

describe("Division", function () {
    it("Divide when both are int", () => {
        assert.strictEqual(calculateNumber("DIVIDE", 1, 3), 0.3333333333333333);
    });

    it("Divide when a: float", () => {
        assert.strictEqual(calculateNumber("DIVIDE", 1.2, 3), 0.3333333333333333);
    });

    it("Divide when b: float", () => {
        assert.strictEqual(calculateNumber("DIVIDE", 1, 3.7), 0.25);
    });

    it("Divide when a is rounded up & b is rounded down", () => {
        assert.strictEqual(calculateNumber("DIVIDE", 1.7, 3.2), 0.6666666666666666);
    });

    it("Divide when a is rounded down & b is rounded up", () => {
        assert.strictEqual(calculateNumber("DIVIDE", 1.2, 3.7), 0.25);
    });

    it("Divide when both are rounded down", () => {
        assert.strictEqual(calculateNumber("DIVIDE", 1.1, 3.2), 0.3333333333333333);
    });

    it("Divide when both are rounded up", () => {
        assert.strictEqual(calculateNumber("DIVIDE", 1.9, 3.6), 0.5);
    });

    it("Divide when a = 0", () => {
        assert.strictEqual(calculateNumber("DIVIDE", 0, 42), 0);
    });

    it("Divide when b = 0", () => {
        assert.strictEqual(calculateNumber("DIVIDE", 42, 0), "Error");
    });
});

describe("Error", function () {
    it("Type is not a string.", () => {
        assert.strictEqual(calculateNumber(2, 1, 3), "Error");
    });
});