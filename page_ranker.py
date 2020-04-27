import numpy as np
import JsonToMatrix


class PageRanker:
    def __init__(self, backlink_matrix):
        self.backlink_matrix = backlink_matrix

    def run(self, num_iterations: int = 100, d: float = 0.85):
        """
        M : numpy array
            adjacency matrix where M_i,j represents the link from 'j' to 'i', such that for all 'j'
            sum(i, M_i,j) = 1

        Each column in the matrix represents the links for column j to other web pages i.
        The diagonal entries will be zero, beucase we don't care about sites linking to themselves.
        If a web site j links to three sites, each entry in the column would be 0.333.

        num_iterations : number of iterations
        d : damping factor

        Returns
        -------
        numpy array
            a vector of ranks such that v_i is the i-th rank from [0, 1],
            v sums to 1
        """
        num_pages = self.backlink_matrix.shape[1]
        page_ranks = np.random.rand(num_pages, 1)

        print("=========================")
        print(f"matrix:\n {self.backlink_matrix}")
        print("=========================")
        print(f"num_pages: {num_pages}")
        print("=========================")
        print(f"random guesses for page_ranks:\n {page_ranks}")
        print("=========================")

        # normalize vectors to enties sum to 1.0
        page_ranks = page_ranks / np.linalg.norm(page_ranks, 1)
        print(f"normalized random guess for page_ranks:\n{page_ranks}")
        print("=========================")

        constant = (1 - d) / num_pages
        M_hat = d * self.backlink_matrix + constant
        print(f"M_hat\n {M_hat}")
        print("=========================")

        for i in range(num_iterations):
            page_ranks = M_hat @ page_ranks

        return page_ranks


if __name__ == "__main__":
    # input_matrix = np.array(
    #     [
    #         [0, 0, 0, 0, 1],
    #         [1, 0, 0, 0, 0],
    #         [1, 0, 0, 0, 0],
    #         [0, 1, 1, 0, 0],
    #         [0, 0, 1, 1, 0],
    #     ]
    # )
    converter = JsonToMatrix.JsonToMatrix("backlinkscraper/adjacency.json")
    input_matrix = converter.getMatrix()

    input_matrix = input_matrix / input_matrix.sum(axis=0, keepdims=1)
    ranker = PageRanker(input_matrix)
    page_ranks = ranker.run(100, 0.85)
    print("=========================")
    print(f"final page_ranks:\n{page_ranks}")
