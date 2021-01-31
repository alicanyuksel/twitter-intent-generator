import re
import urllib.parse
import fpdf
import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    "--input_txt",
    metavar="input_txt",
    type=str,
    required=True,
    help="Txt file path"
)

parser.add_argument(
    "--output_pdf",
    metavar="output_pdf",
    type=str,
    required=True,
    help="Output path for a pdf to generate"
)

parser.add_argument(
    "--output_txt",
    metavar="output_txt",
    type=str,
    required=True,
    help="Output path for a txt to generate"
)

 # Execute the parse_args() method
args = parser.parse_args()


def convert_tweet_to_url(text):
    base_url = "https://twitter.com/intent/tweet?text="
    textencoded = urllib.parse.quote_plus(text)

    return base_url + textencoded, text


def create_new_pdf(data, output_pdf, output_txt):
    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
    pdf.add_font('DejaVu', '', './font/DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 12)

    fl_output = open(output_txt, "w+", encoding="utf-8")

    counter = 1
    for match in data:
        url, text = convert_tweet_to_url(match.group(1))
        text_with_number = f"{counter}. {text}"

        # write on pdf
        pdf.write(5, txt=text_with_number, link=url)
        pdf.write(5, txt="\n\n")

        # write on txt file
        fl_output.write(url)
        fl_output.write("\n\n")

        counter += 1

    # output
    pdf.output(output_pdf)


# define regex to match the string between <tweet> tag
regex = r"<tweet>\n{0,}(.*?)<\/tweet>"

# open file
fl = open(args.input_txt, encoding="utf-8")
all_lines_concatenated = " ".join(fl.readlines())

# regex match
matches = re.finditer(regex, all_lines_concatenated, re.MULTILINE | re.DOTALL)


if __name__ == "__main__":

    create_new_pdf(
        data=matches,
        output_pdf=args.output_pdf,
        output_txt=args.output_txt
    )
