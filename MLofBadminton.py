专业人员练球特征：打球次数多的前提下（一周起码4次），采用多球训练或者具体的步伐重复练习等。
然而我们属于业余人员，我们同事的打球特征是次数少，包括我也是次数少。所以我练球不采用专业人员的练球方法。
而是采用机器学习workflow的思想：
      Workflow:
      1.	Ask a right question .                                                     1.怎么让球擦网而过？
      2.	Correct algorithm to iterate.                                        2. 控制变量法: 球有很多变量：球速、球的高度、球的远度、球的左
                                                                                                      右落点、人的站位等，这些都是变量。假如现在调整球打过去的高
                                                                                                      度，就得保持其他变量都不变的前提下，采用二分法来迭代，就像
                                                                                                      猜数字一样。
      3.	Adjust the parameters and optimize the target.      3. 现在变量只有高度，高了就往下打，低了就 往上打。这样不断地  
                                                                                                      来靠近最优点（擦网）

     所以，如果业余的人能贯彻这个思想去学习，即使一周只打一次，我相信这也是一个快速提高羽毛球的方法，说不定还能     
	 打赢专业的人呢，就像不会下围棋的AlphaGo工程师却打败了李世石。
