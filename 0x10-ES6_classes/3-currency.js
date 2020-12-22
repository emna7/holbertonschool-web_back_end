export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }


  displayFullCurrency() {
    return (`${this.name} (${this.code})`);
  }

  set name(newName) {
    this._name = newName;
  }

  set code(newCode) {
    this._name = newCode;
  }

  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }
}
