# Circuit Challenges

In the next few sections there are 4 challenges for you to complete. Each time you build a circuit that completes a challenge, we'd like you to record your solution into a shared Jamboard. Right now, we'd like one member of the group to make a [Jamboard](https://jamboard.google.com/) and share the board with the other small group members. Drag and drop the images for each challenge to organize them, and label them with their challenge number. 

***

### Challenge 1

We saw that a Bell state makes two up-down measurements come out the same, and two left-right measurements always come out the same. Next, let's try and mix it up a bit.

Build a circuit so that two up-down measurements always give different answers.

Click for a hint!
```{toggle}
    Hint (1 of 1): Remember that an X gate flips up to down and down to up.
```

### Challenge 2



Build a circuit so that two left-right measurements always give different answers.

Click for a hint!
```{toggle}
    Hint (1 of 1): Remember that an Z gate flips up to down and down to up.
```

### Challenge 3

Remember that measuring one qubit of a Bell pair gives a random result. For example if you measure up-down, you get up with 50% chance and down with 50% chance. 

It's possible though to use the bottom qubit to guess what the measurement on the top qubit will give. Set-up your circuit like this:

![](images/setup.PNG)
<br>
Leave the measurement of the top qubit as up-down, and keep the measuring block at the end of your wire, like shown above. The measurement on the top qubit will be random. But, if you use the other qubit in the right way, you can guess what it will be before you measure! Your challenge is to figure out how. 

Click for a hint!
```{toggle}
    Hint (1 of 1): The measurement blocks don't have to be placed at the end of a wire.
```

### Challenge 4

Remember from the one qubit circuit activity that there was always a way to undo a quantum gate. For example, to undo an X gate you just do another X gate. 

With entanglement, you can sometimes undo a gate on a qubit by doing a gate to a different qubit. 

To explore this, set your top wire up like in the picture below:

![](images/setup2.PNG)

<br>



Set your top wire up like in the picture above. You should always get opposites when you measure both qubits up-down. Without the X gate on the top wire you would always get the same outcome when you measure both qubits the up-down way.

Your challenge is to undo the X gate on the top wire, without touching the top wire! You can only add gates to the bottom wire, but you need to make sure the measurement outcomes always come out the same.


Click for a hint!
```{toggle}
    Hint (1 of 1): The bottom qubit will be coming out the opposite of what you want it to - its down when the top one is up. Remember that an X gate flips down to up.
```




![](images/joey.jpg)