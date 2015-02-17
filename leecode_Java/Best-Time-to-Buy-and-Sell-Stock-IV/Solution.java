/*很好的一道题, 把stock类型题彻底搞透

1) 首先第一个点： 当 交易次数 大于 天数的一半时 ( k > len/2 ) ， 最大交易额与II 的思路一样，只要求出所有上升的增加值累加 (prices[i] + prices[i - 1])

2) 然后是如果 k < len / 2. 其实与 III 思路一样，III 是当k ＝ 2. 我们需要用两个DP 维护两个值： 
global[i][j] : 表示 第 i 天交易最多j 次的最大收益值，也就是最后我们要求的答案 
local[i][j]: 表示 第 i 天交易最多第 j 次的最好收益值 (今天必须要卖出 作为最后一次交易)

global[i][j] = max(global[i - 1][j], local[i][j]): 
golobal 取的是 当前第i天恰好第j次交易的最好收益值，与前一天完成的j次交易取得的最大收益，的最大值。 (贪心 保证最大的结果) 
local[i][j] = max(global[i - 1][j - 1] + max(dif, 0), local[i - 1][j] + dif) 
local 会有两种情况： 
情况1：如果local[i - 1][j] 完成了j次交易，那么今天再交易一次（不会增加交易次数，以为交易的连续性：第一天买进第二天卖出再买进，第三天卖出 与第一天买进第三天卖出是相等的） 
情况2：之前 第i-1天已经完成了j -1次交易，那么今天必须完成最后一次交易，有两种选择，如果dif 大于0，说明是赚钱的，如果小于0，就不累加，相当于第i天买进然后卖出，收益为0

时间复杂度为 O(n * k)， 空间 只维护当天的值即可，所以最优是O(k)
*/
public class Solution {
    public int maxProfit(int k, int[] prices) {
        int n = prices.length;
        if(n < 2) return 0;
        if(k > n / 2){
            int res = 0;
            for(int i = 1; i < n; i++){
                if(prices[i] - prices[i - 1] > 0) res += prices[i] - prices[i -1];
            }
            return res;
        }
        int[][] global = new int[n][k + 1];
        int[][] local = new int[n][k + 1];
        for(int i = 1; i < n; i++){
            for(int j = 1; j <= k; j++){
                int dif = prices[i] - prices[i - 1];
                local[i][j] = Math.max(global[i - 1][j - 1] + Math.max(dif, 0), local[i - 1][j] + dif);
                global[i][j] = Math.max(local[i][j], global[i - 1][j]);
            }
        }
        return global[n - 1][k];
    }
}
