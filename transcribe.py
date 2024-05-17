import os
import argparse

def generate_esd_list(in_dir, out_file):
    entries = []
    print(f"in_dir: {in_dir}")
    print(f"out_file: {out_file}")
    speakers = [d for d in os.listdir(in_dir) if os.path.isdir(os.path.join(in_dir, d))]
    print(f"speakers: {speakers}")
    for speaker in speakers:
        speaker_dir = os.path.join(in_dir, speaker)
        wav_files = [f for f in os.listdir(speaker_dir) if f.endswith(".wav")]
        for wav_file in wav_files:
            wav_path = os.path.join(speaker_dir, wav_file)
            lab_file = os.path.splitext(wav_file)[0] + ".lab"
            lab_path = os.path.join(speaker_dir, lab_file)
            if os.path.isfile(lab_path):
                with open(lab_path, "r", encoding="utf-8") as f:
                    text = f.read().strip()
                entries.append(f"{wav_file}|{speaker}|ZH|{text}")

    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(entries))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--in_dir", type=str, required=True, help="Path to the input directory")
    parser.add_argument("--out_file", type=str, required=True, help="Path to the output esd.list file")
    args = parser.parse_args()

    generate_esd_list(args.in_dir, args.out_file)
    print(f"esd.list file has been generated at {args.out_file}")

