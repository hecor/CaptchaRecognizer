for i in {0..99}
do
	wget https://trade.gtja.com/webtrade/commons/verifyCodeImage.jsp?ran=0.5582681659143418
	mv verifyCodeImage.jsp\?ran\=0.5582681659143418 testsets/test$i.jpg
done

