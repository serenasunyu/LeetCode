
var RecentCounter = function() {
    // Brute Force
    // this.stream = [];
    
    // Two Pointer
    this.requests = [null];
    this.front = 1;
    this.rear = 0;
};


/** 
 * @param {number} t
 * @return {number}
 */
RecentCounter.prototype.ping = function(t) {
    // this.stream.push(t);

    // while(this.stream[0] < t - 3000){
    //     this.stream.shift();
    // }
    // return this.stream.length;

    this.requests.push(t);
    this.rear++;
    let range = [t - 3000, t];
    while(this.requests[this.front] < range[0]){
        this.front++;
    }
    return this.rear - this.front + 1;
};

/** 
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */
