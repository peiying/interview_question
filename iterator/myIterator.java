package peiying.com;

import java.util.Collection;
import java.util.Iterator;
import java.util.NoSuchElementException;

/*Contained in the provided workspace is cocI, the start of a class that implements an Iterator that can be used to iterate a Collection of Collections. The Collection of Collections is passed into the constructor of the class. The Iterator should iterate through the contents depth-first.

For example, if the Collection of Collections looks like the following:

[0] – [“A”, “B”, “C”] 
[1] – [“D”] 
[2] – [“E”, “F”] 
The iterator should then return the contents in the following order: “A”, “B”, “C”, “D”, “E”, “F”

Q.Provide implementations for the hasNext() and next() methods in cocI
*/
public class myIterator<T> implements Iterator<T>{
	private Iterator<Collection<T>> outerIterator;
	private Iterator<T> innerIterator;

	public myIterator(Collection<Collection<T>> collOfcoll) {
		this.outerIterator = collOfcoll.iterator();
		helperCollection();
	}
	@Override
	public boolean hasNext() {
		return this.innerIterator != null && this.innerIterator.hasNext();
	}
	@Override
	public T next() {
		if(this.innerIterator == null){
			throw new NoSuchElementException();
		}
		T result = this.innerIterator.next();
		helperCollection();
	    return result;
	}
	private void helperCollection(){
		while((this.innerIterator == null || !this.innerIterator.hasNext())
				&& this.outerIterator.hasNext()){
			this.innerIterator = this.outerIterator.next().iterator();
		}
	}
}
