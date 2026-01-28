class FuvBuilder:
    """
    Creates the PUM based on the PUV and the PUM and PUV.
    """

    def build(self, puv: list[bool], pum: list[list[bool]]) -> list[bool]:
        """
        Constructs a 15x1 vector of bools to be used in decide
        representing the final values for deciding wether to launch

        :param puv: A 15-element boolean vector from input.
        :param pum: A 15x15 matrix of bools.
        :return: A 15x15 matrix representing the PUV.
        """
        fuv = [False for _ in range(15)]
        # If an entire row (i) of the PUM is True -> FUV[i] is set to true
        rowIsTrue = True
        index = 0
        for i in pum:
            for j in range(15):
                if i[j] != None:
                    if i[j] == False:
                        rowIsTrue = False
                        break
            if rowIsTrue == True:
                fuv[index] = True
            rowIsTrue = True
            index += 1

        # Check through the PUV, if any element i is True ->FUV[i]=True
        for i in range(15):
            if puv[i] == False:
                fuv[i] = True
        return fuv


# Export a singleton
DefaultFuvBuilder = FuvBuilder()
