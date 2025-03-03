def dht_hash(text, seed=0, maximum=2**10):
    """ FNV-1a Hash Function. """
    fnv_prime = 16777619
    offset_basis = 2166136261
    h = offset_basis + seed
    for char in text:
        h = h ^ ord(char)
        h = h * fnv_prime
    return h % maximum


def contains(begin, end, node):
    """Check node is contained between begin and end in a ring."""
    # Se os nós estiverem todos na mesma volta
    if begin <  end:
        return begin < node  <= end
    else :
        # retorna True se estiver no intervalo entre o (incio e 128) e (0 e fim)
        return begin < node or node < end
