from game import Game
from corrupted_chess_file_error import *
from player import Player
from piece import Piece
from board import Board


class ChunkIO(object):

    def load_game(self, input):
        """
        @note:This is the game object this method will fill with data. The object
               is returned when the END chunk is reached.
        """
        self.game = Game()

        try:

            # Read the file header and the save date

            header = self.read_fully(8, input)
            date = self.read_fully(8, input)

            # Process the data we just read.
            # NOTE: To test the line below you must test the class once with a broken header

            header = ''.join(header)
            date = ''.join(date)
            if not str(header).startswith("SHAKKI"):
                raise CorruptedChessFileError("Unknown file type")

            # The version information and the date are not used in this
            # exercise

            # *************************************************************
            #
            # EXERCISE
            #
            # ADD CODE HERE FOR READING THE
            # DATA FOLLOWING THE MAIN HEADERS
            #
            #
            # *************************************************************
            komment = self.read_fully(5, input)
            kommentti = self.extract_chunk_name(komment)
            pituus = self.extract_chunk_size(komment)

            lauta = Board()
            end = False
            q = 0
            while True:
                #print(kommentti)
                if kommentti == "CMT":
                    data = self.read_fully(pituus, input)

                elif kommentti == "PLR":
                    data = self.read_fully(pituus, input)
                    nim_var = data[0]

                    nim_pit = int(data[1])
                    nimi = []
                    for x in range(0, nim_pit):
                        nimi.append(data[x+2])
                    nimi = ''.join(nimi)

                    if nim_var == "M":
                        player = Player(nimi, Player.BLACK)
                        q += 1
                    elif nim_var == "V":
                        player = Player(nimi, Player.WHITE)
                        q +=1

                    self.game.add_player(player)

                    list_iterator = iter(data)
                    for i in range(0, nim_pit + 2):
                        next(list_iterator)
                    for element in list_iterator:
                        #print("Elementti:",element)
                        if element == "K":
                            a = str(next(list_iterator))
                            b = str(next(list_iterator))
                            nappula = Piece(player, Piece.KING)
                            key = (a, b)
                            x = lauta.column_char_to_integer(a)
                            y = lauta.row_char_to_integer(b)
                            if 0 <= x < 8 and 0 <= y < 8 and lauta.is_free(x, y):
                                lauta.__setitem__(key, nappula)
                            else:
                                raise CorruptedChessFileError("Place allready taken")
                        elif element == "D":
                            a = str(next(list_iterator))
                            b = str(next(list_iterator))
                            nappula = Piece(player, Piece.QUEEN)
                            key = (a, b)
                            x = lauta.column_char_to_integer(a)
                            y = lauta.row_char_to_integer(b)
                            if 0 <= x < 8 and 0 <= y < 8 and lauta.is_free(x, y):
                                lauta.__setitem__(key, nappula)
                            else:
                                raise CorruptedChessFileError("Place allready taken")
                        elif element == "T":
                            a = str(next(list_iterator))
                            b = str(next(list_iterator))
                            nappula = Piece(player, Piece.ROOK)
                            key = (a, b)
                            x = lauta.column_char_to_integer(a)
                            y = lauta.row_char_to_integer(b)
                            if 0 <= x < 8 and 0 <= y < 8 and lauta.is_free(x, y):
                                lauta.__setitem__(key, nappula)
                            else:
                                raise CorruptedChessFileError("Place allready taken")
                        elif element == "L":
                            a = str(next(list_iterator))
                            b = str(next(list_iterator))
                            nappula = Piece(player, Piece.BISHOP)
                            key = (a, b)
                            x = lauta.column_char_to_integer(a)
                            y = lauta.row_char_to_integer(b)
                            if 0 <= x < 8 and 0 <= y < 8 and lauta.is_free(x, y):
                                lauta.__setitem__(key, nappula)
                            else:
                                raise CorruptedChessFileError("Place allready taken")

                        elif element == "R":
                            a = str(next(list_iterator))
                            b = str(next(list_iterator))
                            nappula = Piece(player, Piece.KNIGHT)
                            key = (a, b)
                            x = lauta.column_char_to_integer(a)
                            y = lauta.row_char_to_integer(b)
                            if 0 <= x < 8 and 0 <= y < 8 and lauta.is_free(x, y):
                                lauta.__setitem__(key, nappula)
                            else:
                                raise CorruptedChessFileError("Place allready taken")
                        elif element.islower():
                            b = str(next(list_iterator))
                            key = (element, b)
                            nappula = Piece(player, Piece.PAWN)
                            x = lauta.column_char_to_integer(element)
                            y = lauta.row_char_to_integer(b)

                            if 0 <= x < 8 and 0 <= y < 8 and lauta.is_free(x, y):
                                lauta.__setitem__(key, nappula)
                            else:
                                raise CorruptedChessFileError("Place allready taken")
                        else:
                            a = str(next(list_iterator))
                            b = str(next(list_iterator))
                            raise CorruptedChessFileError("fake pieces like Ha4")

                elif kommentti == "***":
                    data = self.read_fully(pituus, input)


                elif kommentti == "END":
                    end = True
                    break

                else:
                    data = self.read_fully(pituus, input)

                if input.tell() < 1:
                    raise CorruptedChessFileError("No 'END' in file")

                komment = self.read_fully(5, input)
                kommentti = self.extract_chunk_name(komment)
                pituus = self.extract_chunk_size(komment)

            if q != 2:
                raise CorruptedChessFileError("Player missing")

            self.game.set_board(lauta)
            # If we reach this point the Game-object should now have the proper players and
            # a fully set up chess board. Therefore we might as well return it.

            return self.game

        except OSError:
            # To test this part the stream would have to cause an
            # OSError. That's a bit complicated to test. Therefore we have
            # given you a "secret tool", class BrokenReader, which will throw
            # an OSError at a requested position in the stream.
            # Throw the exception inside any chunk, but not in the chunk header.
            raise CorruptedChessFileError("Reading the chess data failed 1.")




    # HELPER METHODS -------------------------------------------------------



    def extract_chunk_size(self, chunk_header):
        """
        Given a chunk header (an array of 5 chars) will return the size of this
        chunks data.

        @param chunk_header:
                   a chunk header to process (str)
        @return: the size (int) of this chunks data
        """


        # subtracting the ascii value of the character 0 from
        # a character containing a number will return the
        # number itself

        return int( ''.join( chunk_header[3:5] ) )


    def extract_chunk_name(self, chunk_header):
        """
        Given a chunk header (an array of 5 chars) will return the name of this
        chunk as a 3-letter String.

        @param chunk_header:
                   a chunk header to process
        @return: the name of this chunk
        """
        return ''.join( chunk_header[0:3] )


    def read_fully(self, count, input):
        """
        The read-method of the Reader class will occasionally read only part of
        the characters that were requested. This method will repeatedly call read
        to completely fill the given buffer. The size of the buffer tells the
        algorithm how many bytes should be read.

        @param count:
                   How many characters are read
        @param input:
                   The character stream to read from
        @raises: OSError
        @raises: CorruptedChessFileError
        """
        read_chars = input.read( count )

        # If the file end is reached before the buffer is filled
        # an exception is thrown.
        if len(read_chars) != count:
                raise CorruptedChessFileError("Unexpected end of file.")

        return list(read_chars)




