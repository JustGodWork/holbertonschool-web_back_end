const { assert, expect } = require("chai");
const sinon = require("sinon");
const Utils = require("./utils.js");

const sendPaymentRequestToApi = require("./3-payment.js");

describe("sendPaymentRequestToApi", function () {
  let stub;
  let spy;

  this.beforeEach(() => {
    stub = sinon.stub(Utils, "calculateNumber").returns(10);
    spy = sinon.spy(console, "log");
  });

  this.afterEach(() => {
    stub.restore();
    spy.restore();
  });

  it("should call Utils.calculateNumber with correct args", () => {
    sendPaymentRequestToApi(100, 20);

    expect(stub.calledOnce).to.be.true;
    expect(stub.calledWith("SUM", 100, 20)).to.be.true;
    expect(spy.calledOnceWithExactly("The total is: 10")).to.be.true;

    spy.restore();
  });
});
