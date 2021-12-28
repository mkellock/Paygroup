# PayGroup Technical Test

Sample project for the Paygroup technical test :)

## Infrastructure as Code
A regular CF file, run as usual

## Code Development

- Navigate to: `./FizzBuzz/`
- Compile with: `docker build -t paygroup .`
- Run with: `docker run --rm -e "FIZZ_BUZZ_MIN=1" -e "FIZZ_BUZZ_MAX=40" paygroup` (replacing FIZZ_BUZZ_MIN and FIZZ_BUZZ_MAX with desired inputs)

Note: this app assumes happy path, does not validate for erronious environment variables
