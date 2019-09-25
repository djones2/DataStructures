package comparator;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import java.util.Comparator;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

import org.junit.Test;
import org.junit.Before;
import java.util.Collections;

public class TestCases
{
   private static final Song[] songs = new Song[] {
         new Song("Decemberists", "The Mariner's Revenge Song", 2005),
         new Song("Rogue Wave", "Love's Lost Guarantee", 2005),
         new Song("Avett Brothers", "Talk on Indolence", 2006),
         new Song("Gerry Rafferty", "Baker Street", 1998),
         new Song("City and Colour", "Sleeping Sickness", 2007),
         new Song("Foo Fighters", "Baker Street", 1997),
         new Song("Queen", "Bohemian Rhapsody", 1975),
         new Song("Gerry Rafferty", "Baker Street", 1978)
      };

   @Test
   public void testArtistComparator()
   {
      ArtistComparator compArtist = new ArtistComparator();
      assertTrue(compArtist.compare(songs[0], songs[1]) < 0);
   }

   @Test
   public void testArtistComparator2()
   {
      ArtistComparator compArtist = new ArtistComparator();
      assertTrue(0 < compArtist.compare(songs[5], songs[2]));
   }

   @Test
   public void testLambdaTitleComparator()
   {
      Comparator<Song> TitleComparator = (Song s1, Song s2) -> s1.getTitle().compareTo(s2.getTitle());
      Song s1 =  new Song("Decemberists", "The Mariner's Revenge Song", 2005);
      Song s2 =  new Song("Rogue Wave", "Love's Lost Guarantee", 2005);
      assertTrue(TitleComparator.compare(s1, s2) > 0);

   }

   @Test
   public void testLambdaTitleComparator2()
   {
      Comparator<Song> TitleComparator = (Song s1, Song s2) -> s1.getTitle().compareTo(s2.getTitle());
      Song s1 =  new Song("Decemberists", "The Mariner's Revenge Song", 2005);
      Song s2 =  new Song("Rogue Wave", "Love's Lost Guarantee", 2005);
      assertTrue(TitleComparator.compare(s1, s1) == 0);
   }

   @Test
   public void testYearExtractorComparator()
   {
      Comparator<Song> YearComparator = (Song s1, Song s2) -> s1.getYear() - s2.getYear();
      Song s1 =  new Song("Decemberists", "The Mariner's Revenge Song", 2005);
      Song s2 =  new Song("Rogue Wave", "Love's Lost Guarantee", 2005);
      Song s3 =  new Song("Queen", "Bohemian Rhapsody", 1975);
      assertTrue(YearComparator.compare(s1, s2) == 0);
   }

   @Test
   public void testYearExtractorComparator2()
   {
      Comparator<Song> YearComparator = (Song s1, Song s2) -> s1.getYear() - s2.getYear();
      Song s1 =  new Song("Decemberists", "The Mariner's Revenge Song", 2005);
      Song s2 =  new Song("Rogue Wave", "Love's Lost Guarantee", 2005);
      Song s3 =  new Song("Queen", "Bohemian Rhapsody", 1975);
      assertTrue(YearComparator.compare(s3, s1) < 0);
   }

   @Test
   public void testComposedComparator()
   {
      Comparator<Song> Compose = (Song s1, Song s2) -> {
         if (s1.getArtist().equals(s2.getArtist())) {
            return s1.getYear() - s2.getYear();
         }
         else {
            return s1.getArtist().compareTo(s2.getArtist());
         }
      };
      assertTrue(Compose.compare(songs[3], songs[7]) > 0);
   }

   @Test
   public void testComposedComparator2()
   {
      Comparator<Song> Compose = (Song s1, Song s2) -> {
         if (s1.getArtist().equals(s2.getArtist())) {
            return s1.getYear() - s2.getYear();
         }
         else {
            return s1.getArtist().compareTo(s2.getArtist());
         }
      };
      assertTrue(Compose.compare(songs[3], songs[0]) > 0);
   }

   @Test
   public void testThenComparing()
   {
      Comparator<Song> ArtistComparator = (Song s1, Song s2) -> s1.getArtist().compareTo(s2.getArtist());
      Comparator<Song> YearComparator = (Song s1, Song s2) -> s1.getYear() - s2.getYear();
      ComposedComparator Comp = new ComposedComparator(ArtistComparator, YearComparator);
      assertTrue(Comp.compare(songs[3], songs[7]) > 0);
   }

   @Test
   public void testThenComparing2()
   {
      Comparator<Song> ArtistComparator = (Song s1, Song s2) -> s1.getArtist().compareTo(s2.getArtist());
      Comparator<Song> YearComparator = (Song s1, Song s2) -> s1.getYear() - s2.getYear();
      ComposedComparator Comp = new ComposedComparator(ArtistComparator, YearComparator);
      assertTrue(Comp.compare(songs[3], songs[0]) > 0);

   }

   @Test
   public void runSort()
   {
      List<Song> songList = new ArrayList<>(Arrays.asList(songs));
      List<Song> expectedList = Arrays.asList(
              new Song("Avett Brothers", "Talk on Indolence", 2006),
              new Song("City and Colour", "Sleeping Sickness", 2007),
              new Song("Decemberists", "The Mariner's Revenge Song", 2005),
              new Song("Foo Fighters", "Baker Street", 1997),
              new Song("Gerry Rafferty", "Baker Street", 1978),
              new Song("Gerry Rafferty", "Baker Street", 1998),
              new Song("Queen", "Bohemian Rhapsody", 1975),
              new Song("Rogue Wave", "Love's Lost Guarantee", 2005)
      );

      Comparator<Song> composed = (Song s1, Song s2) -> {
         if (s1.getArtist().equals(s2.getArtist())) {
            if (s1.getTitle().equals(s2.getTitle())) {
               return s1.getYear() - s2.getYear();
            }
            else {
               return s1.getTitle().compareTo(s2.getTitle());
            }
         }
         else {
            return s1.getArtist().compareTo(s2.getArtist());
         }
      };

      songList.sort(composed);

      assertEquals(songList, expectedList);
   }
}
