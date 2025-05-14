const { assert, expect } = require("chai");
const sinon = require("sinon");
const Utils = require("./utils.js");

const sendPaymentRequestToApi = require("./3-payment.js");

describe("sendPaymentRequestToApi", function () {
  let spy;

  this.beforeEach(() => {
    spy = sinon.spy(console, "log");
  });

  this.afterEach(() => {
    spy.restore();
  });

  it("should call Utils.calculateNumber with correct args", () => {
    sendPaymentRequestToApi(100, 20);

    expect(spy.calledOnce).to.be.true;
    expect(spy.calledOnceWithExactly("The total is: 120")).to.be.true;

    spy.restore();
  }),
    it("should call Utils.calculateNumber with correct args", () => {
      sendPaymentRequestToApi(10, 10);

      expect(spy.calledOnce).to.be.true;
      expect(spy.calledOnceWithExactly("The total is: 20")).to.be.true;
    });
});
