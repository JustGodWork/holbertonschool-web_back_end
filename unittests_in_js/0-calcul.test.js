const assert = require("assert");
const calculateNumber = require("./0-calcul");

describe("calculateNumber", function () {
  it("Sum when both are integers.", () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it("Sum when b is a float.", () => {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it("Sum when a is rounded down & b is rounded up.", () => {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it("Sum when a is a float.", () => {
    assert.strictEqual(calculateNumber(1.2, 3), 4);
  });

  it("Sum when a is rounded up & b is rounded down.", () => {
    assert.strictEqual(calculateNumber(1.7, 3.2), 5);
  });

  it("Sum when both are rounded up.", () => {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
});
