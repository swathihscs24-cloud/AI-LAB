def evaluate_propositional_kb(variables, kb_sentences, queries):
    """
    Constructs a truth table for any propositional logic knowledge base,
    identifies models, and checks entailment for given queries.
    
    :param variables: List of variable names (e.g., ['P', 'Q', 'R'])
    :param kb_sentences: List of lambda functions representing KB sentences
    :param queries: Dictionary of query names mapped to lambda functions
    """
    num_vars = len(variables)
    
    # Print dynamic header
    header = "".join([f"{v:<6}" for v in variables])
    for i in range(len(kb_sentences)):
        header += f"KB{i+1:<6}"
    header += f"{'KB True?':<10}"
    print(header)
    print("-" * len(header))

    models = []

    # Generate all truth value combinations without itertools (using recursion)
    def get_combinations(n):
        if n == 0:
            yield []
            return
        for rest in get_combinations(n - 1):
            for val in [True, False]:
                yield rest + [val]

    # Evaluate each combination
    for combo in get_combinations(num_vars):
        # Map variables to their truth values for this row
        env = dict(zip(variables, combo))
        
        # Evaluate all KB sentences using keyword arguments
        kb_results = [func(**env) for func in kb_sentences]
        is_kb_true = all(kb_results)
        
        if is_kb_true:
            models.append(env)
            
        # Format and print the row
        row_str = "".join([f"{str(env[v]):<6}" for v in variables])
        row_str += "".join([f"{str(res):<6}" for res in kb_results])
        row_str += f"{str(is_kb_true):<10}"
        print(row_str)

    print("\n" + "="*40)
    print("Models where KB is True:")
    if not models:
        print("No models found (KB is inconsistent/unsatisfiable).")
    else:
        for i, m in enumerate(models, 1):
            model_str = ", ".join([f"{k}={v}" for k, v in m.items()])
            print(f"Model {i}: {{{model_str}}}")

    print("\nEntailment Results:")
    for name, query_func in queries.items():
        # KB entails query iff query is true in ALL models where KB is true
        entails = all(query_func(**m) for m in models) if models else True
        print(f"Does KB entail {name}? -> {'Yes' if entails else 'No'}")

# ==========================================
# Example Calling the Function for Your Problem
# ==========================================
if __name__ == "__main__":
    # Define your propositional variables
    vars_list = ['P', 'Q', 'R']
    
    # Define your KB sentences as lambda functions
    # 1. Q -> P  -> (~Q or P)
    # 2. P -> ~Q -> (~P or ~Q)
    # 3. Q v R   -> (Q or R)
    kb = [
        lambda P, Q, R: (not Q) or P,
        lambda P, Q, R: (not P) or (not Q),
        lambda P, Q, R: Q or R
    ]
    
    # Define queries you want to check entailment for
    q_to_check = {
        "R": lambda P, Q, R: R,
        "R -> P": lambda P, Q, R: (not R) or P,
        "Q -> R": lambda P, Q, R: (not Q) or R
    }
    
    # Call the generic function
    evaluate_propositional_kb(vars_list, kb, q_to_check)