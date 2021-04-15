import {inject, Getter} from '@loopback/core';
import {DefaultCrudRepository, repository, HasManyRepositoryFactory} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {Batch, BatchRelations, History, State} from '../models';
import {HistoryRepository} from './history.repository';
import {StateRepository} from './state.repository';

export class BatchRepository extends DefaultCrudRepository<
  Batch,
  typeof Batch.prototype.batch_id,
  BatchRelations
> {

  public readonly histories: HasManyRepositoryFactory<History, typeof Batch.prototype.batch_id>;

  public readonly states: HasManyRepositoryFactory<State, typeof Batch.prototype.batch_id>;

  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource, @repository.getter('HistoryRepository') protected historyRepositoryGetter: Getter<HistoryRepository>, @repository.getter('StateRepository') protected stateRepositoryGetter: Getter<StateRepository>,
  ) {
    super(Batch, dataSource);
    this.states = this.createHasManyRepositoryFactoryFor('states', stateRepositoryGetter,);
    this.registerInclusionResolver('states', this.states.inclusionResolver);
    this.histories = this.createHasManyRepositoryFactoryFor('histories', historyRepositoryGetter,);
    this.registerInclusionResolver('histories', this.histories.inclusionResolver);
  }
}
