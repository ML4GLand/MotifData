def describe_motif_set(motif_set):
    print(f"# motifs: {len(motif_set)}")
    print(f"Alphabet: {motif_set.alphabet}")
    print(f"Version: {motif_set.version}")
    print(f"Strands: {motif_set.strands}")
    print(f"Background: {motif_set.background}")
    print(f"Background source: {motif_set.background_source}")

def print_motifs(motif_set, n=None):
    for motif in motif_set:
        print(f"Identifer: {motif.identifier}")
        print(f"Name: {motif.name}")
        print(f"Consensus: {motif.consensus}")
        print(f"PFM: {motif.pfm} with shape {motif.pfm.shape}")
        print()
        if n is not None:
            n -= 1
            if n == 0:
                break

