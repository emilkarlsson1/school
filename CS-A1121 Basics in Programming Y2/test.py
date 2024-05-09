import unittest
from io import StringIO


from chunkIO import ChunkIO
from broken_reader import BrokenReader
from corrupted_chess_file_error import CorruptedChessFileError
from piece import Piece


class Test(unittest.TestCase):

    def test_given_example(self):
        """
        IMPORTANT!

        The test method is allowed here to throw the CorruptedChessFileError.

        The reasons for this are
        1) we expect the code to work
        2) if the code throws this exception the test will self.fail

        This is therefore desired behavior for this test. It also removes the problem
        of untestable code in the catch section.
        """
        test_data = u"SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLR17M5MarkoKa4Ta6b3c3" + u"PLR13V5LAURIKd3Rf1" + u"END00"

        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        #self.input_file = open('game.txt', 'r')
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
        except CorruptedChessFileError:
            self.fail("Loading a correctly structured file caused an exception")

        self.input_file.close()


        self.assertNotEqual(None, game.get_black(), "Loading data self.failed. Player missing.")
        self.assertEqual("Marko" ,game.get_black().get_name(),  "Loading data self.failed. Wrong player name.")


        # Add your own tests, check that the players are ok and that the pieces were correctly placed.
        white = game.get_white()
        black = game.get_black()
        board = game.get_board()

        #print("Pelaaja:", white.name, "väri: Valkoinen")
        #print("Pelaaja:", black.name, "väri: Musta")

        self.assertEqual("Marko",game.get_black().get_name(), "Musta väärin")
        self.assertEqual("LAURI", game.get_white().get_name(), "Valkoinen väärin")
        self.assertEqual(0,board.get_piece(0, 3).get_type(), "kuningas ei ole a4:ssä")
        self.assertEqual(4, board.get_piece(0, 5).get_type(), "Rook ei ole a6:ssä")
        self.assertEqual(5, board.get_piece(1, 2).get_type(), "Sotilas ei ole b3:ssä")
        self.assertEqual(5, board.get_piece(2, 2).get_type(), "Sotilas ei ole c3:ssä")
        self.assertEqual(0, board.get_piece(3, 2).get_type(), "kuningas ei ole d3:ssä")
        self.assertEqual(3, board.get_piece(5, 0).get_type(), "Knight ei ole a6:ssä")
        self.assertEqual(0,white.get_color(),"Valkoinen väri väärin")
        self.assertEqual(1, black.get_color(), "Musta väri väärin")


        """
        print("Pelilauta:")
        for x in range(0, 8):
            for y in range(0,8):
                piece = board.get_piece(x, y)
                if piece != None:
                    yht = board.get_piece(x, y)
                    print(piece.get_type(), end=' ')
                else:
                    print("6", end=' ')
            print()
        """

    def testOSError(self):
        """
        This test was designed to test the catch code in method load_game.
        """
        test_data = u"SHAKKI1205072001"\
            + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..."\
            + u"PLR17M5MarkoKa4Ta6b3c3" + "PLR13V5LAURIKd3Rf1" + "END00"

        #original_file = open('game.txt', 'r')

        # Adding a brokenreader allows raising simulated exceptions
        self.input_file = BrokenReader(test_data, 26)

        check_this = None
        try:
            ChunkIO().load_game(self.input_file)
        except CorruptedChessFileError as e:
            check_this = e

        # Note that initially your code does not read past the file header
        # so this test will fail.

        self.assertNotEqual(None, check_this, "A CorruptedChessFileError was not raised.")

        try:
            self.input_file.close()
            self.fail("Closing a file did not cause an exception.")
        except OSError:
            """All ok"""

        self.input_file.close_really()


    def close_silently(self, r):
        try:
            r.close()
        except OSError:
            """ignore"""


if __name__ == "__main__":
    unittest.main()
