module voting_machine (
    input wire clk,
    input wire rst,
    input wire a,
    input wire b,
    input wire c,
    input wire d,
    output reg [3:0] vote1,
    output reg [3:0] vote2,
    output reg [3:0] vote3,
    output reg [3:0] total_votes
);

    wire e, f, g;

    assign e = a & ~b & ~c;
    assign f = ~a & b & ~c;
    assign g = ~a & ~b & c;

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            vote1 <= 4'b0000;
            vote2 <= 4'b0000;
            vote3 <= 4'b0000;
            total_votes <= 4'b0000;
        end else if (d) begin
            if (e) begin
                vote1 <= vote1 + 1;
                total_votes <= total_votes + 1;
            end
            if (f) begin
                vote2 <= vote2 + 1;
                total_votes <= total_votes + 1;
            end
            if (g) begin
                vote3 <= vote3 + 1;
                total_votes <= total_votes + 1;
            end
        end
    end

endmodule
