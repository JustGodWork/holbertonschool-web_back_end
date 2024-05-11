/* eslint-disable */
import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Amount must be a number');
    } else {
      this._amount = value;
    }
  }

  get currency() {
    return this._currency;
  }

  set currency(value) {
    if (!(value instanceof Currency)) {
      throw new TypeError('Currency must be an instance of the Currency class');
    } else {
      this._currency = value;
    }
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.displayFullCurrency()}`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw new TypeError('Both amount and conversionRate must be numbers');
    } else {
      return amount * conversionRate;
    }
  }
}
