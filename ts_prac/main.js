var BankAccount = /** @class */ (function () {
    function BankAccount(initialBalance) {
        this.balance = initialBalance;
    }
    BankAccount.prototype.deposit = function (amount) {
        this.balance += amount;
    };
    BankAccount.prototype.getBalance = function () {
        return this.balance;
    };
    return BankAccount;
}());
function main() {
    var myAccount = new BankAccount(1000);
    myAccount.deposit(550);
    console.log(myAccount.getBalance()); // Expect 1500
}
main();
