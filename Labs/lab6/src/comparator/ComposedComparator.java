package comparator;

import java.util.Comparator;

public class ComposedComparator implements Comparator<Song> {
    Comparator<Song> comp1;
    Comparator<Song> comp2;

    public ComposedComparator(Comparator<Song> comp1, Comparator<Song> comp2){
        this.comp1 = comp1;
        this.comp2 = comp2;
    }

    public int compare(Song s1, Song s2) {
        if (comp1.compare(s1, s2) == 0) {
            return comp2.compare(s1, s2);
        } else {
            return comp1.compare(s1, s2);
        }
    }
}
