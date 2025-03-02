
// OOPS Concept (Access modifiers: Private, Publc, Protected and ReadOnly)
class BankAccount {
    private balance: number;
  
    constructor(initialBalance: number) {
      this.balance = initialBalance;
    }
  
    public deposit(amount: number): void {
      this.balance += amount;
    }
  
    public getBalance(): number {
      return this.balance;
    }
  }
  
  function main() {
    const myAccount = new BankAccount(1000);
    myAccount.deposit(550);
    console.log(myAccount.getBalance()); // Expect 1500
  }
  
  main();
  