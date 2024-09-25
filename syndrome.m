% Full script for calculating the syndrome of a linear block code

% Define the parity-check matrix H
H = [1 0 1 0 1 0 1;
        0 1 1 0 0 1 1;
        0 0 0 1 1 1 1]; % Parity-check matrix

% Define the received codeword
received = [1 1 1 1 0 1 0]; % Received codeword

% Call the calculate_syndrome function
syndrome = calculate_syndrome(received, H);

% Display the syndrome
disp('Syndrome:');
disp(syndrome);

% Function definition
function syndrome = calculate_syndrome(received, H)
    % Calculate the syndrome for a given received vector and parity-check matrix H.
    % received: a vector of received bits
    % H: the parity-check matrix

    % Compute the syndrome
syndrome = mod(received * H', 2);
end
