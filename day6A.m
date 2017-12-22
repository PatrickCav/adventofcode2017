function count = day6A(input)

% Initialize some useful values
n = length(input); % number of training examples

count = 0;
original = input;
strings = ['']

while true

    [value, index] = max(input);
    endIndex = value + index;
    size = endIndex + mod(-endIndex, n);
    addition = zeros(1, size);
    addition(index + 1:endIndex) = 1;

    addition = sum(reshape(addition, n, size/n)', 1);
    input(index) = 0;
    input = input + addition

    row = mat2str(input)

    if strcmp(strings, row)
        printf("Equal %s", row);
        break
    end

    strings = [strings; row];
    count = count + 1;
    printf("Count: %d\n", count);
end

end
