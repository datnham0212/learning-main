using System;


class mathQuestion {
    static Random random1 = new Random();
    static Random random2 = new Random();
    int a = random1.Next(1,10);
    int b = random2.Next(1,10);
    
    public void question(){
        Console.WriteLine("What's " + a + " + " + b + "? ");
        int userAnswer = Convert.ToInt32(Console.ReadLine());
        int actualAnswer = a + b;
        
        string result = (userAnswer == actualAnswer) ? "Correct" : "Wrong";
        
        Console.WriteLine(result);
    }
}


class SimpleQuizzes {
  static void Main() {
      Console.WriteLine("What's your name? ");
      string name = Console.ReadLine();
      
      Console.WriteLine("Hi there " + name + ", can you do mental math? ");
      string answer = Console.ReadLine();
      
      if(answer=="Yes" || answer=="y" || answer=="yes" || answer == "Y" || answer == "sure" || answer == "Sure"){
          Console.WriteLine("Ok then, let's play");
          
          mathQuestion mq = new mathQuestion();
          mq.question();
      }
      
      else{
          Console.WriteLine("Maybe next time then");
      }
  }
}
